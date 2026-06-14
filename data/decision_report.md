# Decision Report

- generated_at: 2026-06-14T00:05:28.432773+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6619**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6619, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.03% | **+0.51%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.62% | **+0.97%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.72** / 初期 $100.00 (+67.72%)
- 確定: 1492件 (Win 401 / Loss 476 / Flat 615) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $167.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.06** / 初期 $100.00 (-0.94%)
- 確定: 30件 (Win 11 / Loss 10 / Flat 9) / skip 0件
- 成長率目線: 平均log -0.000315 / 幾何平均 -0.032% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0264 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $99.06

## 5. Latest Market Context

- 更新: 2026-06-14T00:05:24.479558+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64387.1
- Funnel: target 770 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +30.34% | $2,288,006.17 |
| RIF/USDT:USDT | +20.44% | $12,751,058.51 |
| H/USDT:USDT | +18.57% | $17,362,698.72 |
| MEGA/USDT:USDT | +13.67% | $2,918,712.04 |
| BTW/USDT:USDT | +9.78% | $1,753,359.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.17% | +2.21% |
| JCT/USDT:USDT | below_1h_threshold | +1.22% | +1.27% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.98% | +1.02% |
| TRADOOR/USDT:USDT | below_1h_threshold | +0.96% | +1.01% |
| BTW/USDT:USDT | below_1h_threshold | +0.91% | +0.96% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
