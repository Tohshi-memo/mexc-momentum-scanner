# Decision Report

- generated_at: 2026-06-11T16:27:47.276712+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6376**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6376, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.21% | **+0.09%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.01% | **+0.00%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.23% | **+1.34%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.76% | **+1.14%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.54% | **+1.08%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.65** / 初期 $100.00 (+52.65%)
- 確定: 1293件 (Win 332 / Loss 409 / Flat 552) / skip 1644件
- 成長率目線: 平均log +0.000327 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $152.65

## 4. Latest Market Context

- 更新: 2026-06-11T16:27:41.438779+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=62589.7
- Funnel: target 782 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +6.14% | $92,576,866.05 |
| SKYAI/USDT:USDT | +5.76% | $9,763,489.46 |
| HIGH/USDT:USDT | +3.20% | $1,261,521.50 |
| LAB/USDT:USDT | +2.90% | $23,924,969.01 |
| SIREN/USDT:USDT | +2.90% | $5,733,820.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +3.06% | +3.28% |
| HIGH/USDT:USDT | below_1h_threshold | +3.01% | +3.23% |
| LAB/USDT:USDT | below_1h_threshold | +2.82% | +3.03% |
| ZBT/USDT:USDT | below_1h_threshold | +2.69% | +2.91% |
| ALLO/USDT:USDT | below_1h_threshold | +2.62% | +2.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
