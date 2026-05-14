# Decision Report

- generated_at: 2026-05-14T13:33:16.953517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4293**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4293, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.14% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.86% | **+0.73%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.59% | **+0.64%** |
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.28% | **+0.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.29% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.37** / 初期 $100.00 (+20.37%)
- 確定: 348件 (Win 95 / Loss 125 / Flat 128) / skip 506件
- 成長率目線: 平均log +0.000533 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $120.37

## 4. Latest Market Context

- 更新: 2026-05-14T13:33:13.005109+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=79912.8
- Funnel: target 763 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1, 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +56.65% | $8,264,409.15 |
| TROLLSOL/USDT:USDT | +32.39% | $2,258,250.31 |
| PLAY/USDT:USDT | +32.02% | $2,262,145.26 |
| UP/USDT:USDT | +26.64% | $1,769,375.70 |
| RIVER/USDT:USDT | +18.60% | $16,225,652.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +4.80% | +4.56% |
| RIVER/USDT:USDT | below_1h_threshold | +2.90% | +2.66% |
| HYPE/USDT:USDT | below_1h_threshold | +2.77% | +2.52% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.38% | +2.14% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.05% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
