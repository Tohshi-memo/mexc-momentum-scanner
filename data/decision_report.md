# Decision Report

- generated_at: 2026-09-06T02:01:20.923081+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13787**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13787, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.57% | **+0.14%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.25% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.85% | **+1.20%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.09% | **+1.19%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.56% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$863.00** / 初期 $100.00 (+763.00%)
- 確定: 5093件 (Win 1528 / Loss 1661 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $863.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.37** / 初期 $100.00 (+89.37%)
- 確定: 2532件 (Win 706 / Loss 599 / Flat 1227) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0576 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $189.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.90** / 初期 $100.00 (+19.90%)
- 確定: 2404件 (Win 715 / Loss 912 / Flat 777) / pending 6件 / skip 2852件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $119.90

## 6. Latest Market Context

- 更新: 2026-09-06T02:01:11.849014+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79952.6
- Funnel: target 1050 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +45.69% | $104,032,473.06 |
| UAI/USDT:USDT | +29.47% | $7,098,931.65 |
| SUSHI/USDT:USDT | +27.10% | $4,090,427.88 |
| BASECAT/USDT:USDT | +23.88% | $2,004,848.26 |
| UNI/USDT:USDT | +16.30% | $54,987,204.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SUSHI/USDT:USDT | below_1h_threshold | +0.67% | +0.63% |
| BCH/USDT:USDT | below_1h_threshold | +0.51% | +0.46% |
| ARB/USDT:USDT | below_1h_threshold | +0.48% | +0.43% |
| AAVE/USDT:USDT | below_1h_threshold | +0.45% | +0.41% |
| LINK/USDT:USDT | below_1h_threshold | +0.42% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
