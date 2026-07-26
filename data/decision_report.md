# Decision Report

- generated_at: 2026-07-26T00:16:19.881892+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9549**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=9549, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.40% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.40% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.03% | **+0.77%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.71% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$462.31** / 初期 $100.00 (+362.31%)
- 確定: 3377件 (Win 1074 / Loss 1095 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $462.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$138.88** / 初期 $100.00 (+38.88%)
- 確定: 1202件 (Win 334 / Loss 265 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1108 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $138.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.35** / 初期 $100.00 (+8.35%)
- 確定: 593件 (Win 201 / Loss 228 / Flat 164) / pending 1件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000496 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.35

## 6. Latest Market Context

- 更新: 2026-07-26T00:16:14.631833+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64400.1
- Funnel: target 898 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +30.44% | $22,047,013.68 |
| ESPORTS/USDT:USDT | +27.38% | $27,778,891.93 |
| BANK/USDT:USDT | +16.75% | $86,395,311.25 |
| ALLO/USDT:USDT | +16.62% | $18,266,049.05 |
| VELVET/USDT:USDT | +9.52% | $7,938,363.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +1.85% | +1.75% |
| ALLO/USDT:USDT | below_1h_threshold | +1.54% | +1.44% |
| LAB/USDT:USDT | below_1h_threshold | +1.38% | +1.28% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.21% | +1.11% |
| ZRO/USDT:USDT | below_1h_threshold | +1.08% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
