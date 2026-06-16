# Decision Report

- generated_at: 2026-06-16T17:21:33.858851+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6874**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=6874, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.23% | **+0.07%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.85% | **+3.30%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.72%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.54% | **+0.46%** |
| ASK_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.41% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.97** / 初期 $100.00 (+84.97%)
- 確定: 1747件 (Win 460 / Loss 548 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $184.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 129件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0093 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T17:21:28.874471+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=65743.6
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +11.59% | $22,679,511.74 |
| STG/USDT:USDT | +8.66% | $3,297,996.43 |
| BSB/USDT:USDT | +7.40% | $37,786,538.07 |
| ESPORTS/USDT:USDT | +5.92% | $1,556,013.58 |
| TRIA/USDT:USDT | +5.87% | $1,017,927.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.13% | +4.12% |
| VELVET/USDT:USDT | below_1h_threshold | +3.70% | +3.68% |
| WLD/USDT:USDT | below_1h_threshold | +2.67% | +2.66% |
| UNI/USDT:USDT | below_1h_threshold | +2.43% | +2.41% |
| BTW/USDT:USDT | below_1h_threshold | +1.75% | +1.73% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
