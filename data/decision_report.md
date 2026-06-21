# Decision Report

- generated_at: 2026-06-21T06:54:10.313356+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7293**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.64% / filled 20/20。**
- 全期間 MARKET基準: n=7293, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.22% | **+0.32%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.28% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$236.19** / 初期 $100.00 (+136.19%)
- 確定: 2022件 (Win 598 / Loss 662 / Flat 762) / skip 1832件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TNSR/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $236.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 393件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0313 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T06:54:04.669799+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64272.7
- Funnel: target 796 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TNSR/USDT:USDT | +58.43% | $1,484,245.17 |
| BICO/USDT:USDT | +19.19% | $52,768,790.36 |
| LAB/USDT:USDT | +17.88% | $20,698,465.82 |
| RESOLV/USDT:USDT | +16.35% | $4,275,868.34 |
| ALICE/USDT:USDT | +13.93% | $3,599,561.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.34% | +2.27% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.93% | +1.86% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.17% | +1.10% |
| APT/USDT:USDT | below_1h_threshold | +1.13% | +1.06% |
| ENA/USDT:USDT | below_1h_threshold | +1.00% | +0.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
