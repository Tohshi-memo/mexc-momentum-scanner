# Decision Report

- generated_at: 2026-09-19T22:26:10.321896+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15102**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=15102, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +3.82% | **+1.27%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.78% | **+0.70%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.49% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.10% | **+1.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.58% | **+0.23%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | -0.08% | **-0.06%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.18% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6023件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.07** / 初期 $100.00 (+144.07%)
- 確定: 3215件 (Win 890 / Loss 762 / Flat 1563) / skip 5298件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0231 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $244.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2975件 (Win 880 / Loss 1176 / Flat 919) / pending 3件 / skip 3596件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T22:26:01.544299+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81031.2
- Funnel: target 1050 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +60.46% | $40,412,300.17 |
| OFC/USDT:USDT | +44.63% | $1,695,101.07 |
| BANK/USDT:USDT | +11.64% | $2,411,930.34 |
| EVAA/USDT:USDT | +10.74% | $1,134,728.06 |
| CATE/USDT:USDT | +9.68% | $1,524,622.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.57% | +4.61% |
| ONE/USDT:USDT | below_1h_threshold | +1.91% | +1.95% |
| INJ/USDT:USDT | below_1h_threshold | +1.44% | +1.48% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.18% | +1.23% |
| RIVER/USDT:USDT | below_1h_threshold | +0.56% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
