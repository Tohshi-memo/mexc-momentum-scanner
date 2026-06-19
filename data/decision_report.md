# Decision Report

- generated_at: 2026-06-19T22:13:33.690967+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7175**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=7175, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.57% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.23% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.72% | **+0.54%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.43%** |
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.30% | **+0.18%** |
| MARKET_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1969件 (Win 571 / Loss 640 / Flat 758) / skip 1767件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 276件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T22:13:29.338563+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63051.0
- Funnel: target 795 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +28.23% | $10,577,440.82 |
| BLESS/USDT:USDT | +18.73% | $4,577,378.01 |
| BTW/USDT:USDT | +14.58% | $7,733,337.69 |
| RE/USDT:USDT | +11.62% | $66,215,058.58 |
| JTO/USDT:USDT | +9.97% | $4,476,799.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.16% | +2.15% |
| RE/USDT:USDT | below_1h_threshold | +1.91% | +1.90% |
| BICO/USDT:USDT | below_1h_threshold | +1.42% | +1.42% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.32% | +1.32% |
| JTO/USDT:USDT | below_1h_threshold | +1.17% | +1.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
