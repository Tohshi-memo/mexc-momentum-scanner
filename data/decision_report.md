# Decision Report

- generated_at: 2026-09-09T22:06:28.969558+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14123**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.61% / filled 20/20。**
- 全期間 MARKET基準: n=14123, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.95% | **+1.85%** |
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.28% | **+0.90%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.45% | **+0.87%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.90% | **+0.77%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5371件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$195.44** / 初期 $100.00 (+95.44%)
- 確定: 2717件 (Win 746 / Loss 636 / Flat 1335) / skip 4817件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1360 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $195.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.75** / 初期 $100.00 (+18.75%)
- 確定: 2630件 (Win 770 / Loss 1005 / Flat 855) / pending 3件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000389 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VVV/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.75

## 6. Latest Market Context

- 更新: 2026-09-09T22:06:13.285835+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=77988.0
- Funnel: target 1064 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IOST/USDT:USDT | +24.42% | $35,127,487.98 |
| CATE/USDT:USDT | +5.02% | $2,662,130.42 |
| KAS/USDT:USDT | +4.99% | $3,401,262.61 |
| WAVES/USDT:USDT | +3.56% | $1,205,086.27 |
| BTR/USDT:USDT | +1.84% | $1,396,842.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +1.86% | +2.01% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +0.40% | +0.55% |
| SOXS/USDT:USDT | below_1h_threshold | +0.28% | +0.43% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.17% | +0.32% |
| USOIL/USDT:USDT | below_1h_threshold | +0.17% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
