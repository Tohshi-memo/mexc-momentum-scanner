# Decision Report

- generated_at: 2026-07-09T03:38:33.827795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8520**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=8520, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.27% | **+0.13%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$103.06** / 初期 $100.00 (+3.06%)
- 確定トレード: 82件 (TP 29 / SL 52 / EXP 1)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.06
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.69** / 初期 $100.00 (+219.69%)
- 確定: 2708件 (Win 855 / Loss 906 / Flat 947) / skip 2373件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $319.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1289件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-09T03:27:37.227679+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=61904.0
- Funnel: target 851 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +91.71% | $5,920,095.93 |
| SKYAI/USDT:USDT | +27.09% | $8,591,792.76 |
| VANRY/USDT:USDT | +13.43% | $7,099,025.27 |
| ALLO/USDT:USDT | +12.42% | $11,496,460.62 |
| CAP/USDT:USDT | +11.62% | $1,750,587.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +3.55% | +3.31% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.37% | +3.13% |
| UAI/USDT:USDT | below_1h_threshold | +2.50% | +2.26% |
| RE/USDT:USDT | below_1h_threshold | +2.00% | +1.76% |
| BASED/USDT:USDT | below_1h_threshold | +1.59% | +1.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
