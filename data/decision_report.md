# Decision Report

- generated_at: 2026-06-14T14:20:04.150020+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6669**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.68% / filled 20/20。**
- 全期間 MARKET基準: n=6669, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |
| ASK | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.35% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$170.37** / 初期 $100.00 (+70.37%)
- 確定: 1542件 (Win 409 / Loss 488 / Flat 645) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $170.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 58件 (Win 19 / Loss 12 / Flat 27) / skip 22件
- 成長率目線: 平均log -0.000173 / 幾何平均 -0.017% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T14:19:58.955932+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64260.3
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +30.45% | $8,536,627.34 |
| CLO/USDT:USDT | +27.58% | $1,077,449.18 |
| ZKC/USDT:USDT | +27.28% | $1,490,852.10 |
| OPG/USDT:USDT | +21.15% | $1,683,952.33 |
| H/USDT:USDT | +18.50% | $87,851,566.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +4.83% | +4.87% |
| BSB/USDT:USDT | below_1h_threshold | +3.78% | +3.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.52% | +2.56% |
| PYTH/USDT:USDT | below_1h_threshold | +2.22% | +2.26% |
| CHIP/USDT:USDT | below_1h_threshold | +1.23% | +1.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
