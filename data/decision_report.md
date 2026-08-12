# Decision Report

- generated_at: 2026-08-12T13:26:17.113809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11373**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=11373, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.22% | **+1.15%** |
| LIMIT_5PCT | 9/20 | 45.0% | +2.52% | **+1.13%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_BB3S | 4/12 | 33.3% | +2.74% | **+0.91%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.33% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.81% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.13% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.08** / 初期 $100.00 (+506.08%)
- 確定: 3948件 (Win 1232 / Loss 1291 / Flat 1425) / skip 3986件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $606.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.30** / 初期 $100.00 (+47.30%)
- 確定: 1596件 (Win 449 / Loss 374 / Flat 773) / skip 3188件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0502 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $147.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.00** / 初期 $100.00 (+15.00%)
- 確定: 1387件 (Win 416 / Loss 535 / Flat 436) / pending 1件 / skip 1454件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.00

## 6. Latest Market Context

- 更新: 2026-08-12T13:26:10.750546+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=63910.2
- Funnel: target 972 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +92.57% | $5,093,870.63 |
| PROM/USDT:USDT | +59.42% | $10,780,098.16 |
| BR/USDT:USDT | +58.54% | $6,143,992.20 |
| JIMOTHY/USDT:USDT | +55.31% | $2,896,907.51 |
| LSK/USDT:USDT | +31.18% | $4,427,416.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.27% | +4.55% |
| LSK/USDT:USDT | below_1h_threshold | +3.57% | +3.85% |
| SOXL/USDT:USDT | below_1h_threshold | +3.10% | +3.38% |
| SNXX/USDT:USDT | below_1h_threshold | +2.68% | +2.96% |
| APR/USDT:USDT | below_1h_threshold | +2.68% | +2.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
