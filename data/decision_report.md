# Decision Report

- generated_at: 2026-06-14T10:07:54.516754+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6657**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6657, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 9/20 | 45.0% | +0.45% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| ASK | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.58% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.23** / 初期 $100.00 (+71.23%)
- 確定: 1530件 (Win 408 / Loss 486 / Flat 636) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $171.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 57件 (Win 19 / Loss 12 / Flat 26) / skip 11件
- 成長率目線: 平均log -0.000176 / 幾何平均 -0.018% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T10:07:50.463656+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=64504.4
- Funnel: target 770 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +108.11% | $48,464,213.04 |
| BTW/USDT:USDT | +14.62% | $3,297,944.59 |
| VELVET/USDT:USDT | +14.38% | $64,042,659.65 |
| TRADOOR/USDT:USDT | +13.02% | $7,790,712.50 |
| MEGA/USDT:USDT | +11.80% | $4,645,819.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.33% | +1.45% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.78% | +0.91% |
| BLUAI/USDT:USDT | below_1h_threshold | +0.59% | +0.72% |
| H/USDT:USDT | below_1h_threshold | +0.40% | +0.53% |
| BTW/USDT:USDT | below_1h_threshold | +0.32% | +0.44% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
