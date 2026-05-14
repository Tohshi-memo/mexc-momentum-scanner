# Decision Report

- generated_at: 2026-05-14T14:41:09.920643+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4298**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4298, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_BB3S | 4/10 | 40.0% | +2.44% | **+0.98%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.39% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.86% | **+0.73%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.86% | **+0.69%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.77** / 初期 $100.00 (+19.77%)
- 確定: 353件 (Win 95 / Loss 126 / Flat 132) / skip 506件
- 成長率目線: 平均log +0.000511 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.77

## 4. Latest Market Context

- 更新: 2026-05-14T14:41:06.458856+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.80% price=80299.0
- Funnel: target 763 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +71.88% | $11,082,646.04 |
| UP/USDT:USDT | +29.36% | $1,778,335.37 |
| TROLLSOL/USDT:USDT | +27.81% | $2,274,910.15 |
| PLAY/USDT:USDT | +26.26% | $3,239,892.61 |
| ESPORTS/USDT:USDT | +24.87% | $1,308,332.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.65% | +3.85% |
| CFX/USDT:USDT | below_1h_threshold | +4.56% | +3.77% |
| IRYS/USDT:USDT | below_1h_threshold | +4.52% | +3.73% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +4.36% | +3.57% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.85% | +3.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
