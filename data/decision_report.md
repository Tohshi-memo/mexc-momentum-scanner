# Decision Report

- generated_at: 2026-06-24T08:11:36.224613+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7469**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7469, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.51% | **+0.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.93** / 初期 $100.00 (+1.93%)
- 確定トレード: 32件 (TP 12 / SL 20 / EXP 0)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.66** / 初期 $100.00 (+131.66%)
- 確定: 2100件 (Win 622 / Loss 696 / Flat 782) / skip 1930件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $231.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.17** / 初期 $100.00 (+7.17%)
- 確定: 332件 (Win 94 / Loss 89 / Flat 149) / skip 548件
- 成長率目線: 平均log +0.000209 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0376 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $107.17

## 5. Latest Market Context

- 更新: 2026-06-24T08:11:31.789786+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62609.2
- Funnel: target 807 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +38.27% | $14,538,904.24 |
| SLX/USDT:USDT | +35.45% | $2,941,112.88 |
| BEAT/USDT:USDT | +27.00% | $86,145,290.60 |
| SAHARA/USDT:USDT | +17.75% | $1,501,862.85 |
| ID/USDT:USDT | +16.41% | $1,314,020.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.42% | +2.45% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.23% | +2.26% |
| KORU/USDT:USDT | below_1h_threshold | +2.22% | +2.25% |
| RENDER/USDT:USDT | below_1h_threshold | +1.76% | +1.80% |
| GRASS/USDT:USDT | below_1h_threshold | +1.71% | +1.75% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
