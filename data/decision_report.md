# Decision Report

- generated_at: 2026-08-25T00:11:24.735792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12553**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12553, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.83% | **+0.17%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.48% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +3.52% | **+2.46%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.16% | **+2.21%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.69% | **+1.61%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.51% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$691.25** / 初期 $100.00 (+591.25%)
- 確定: 4534件 (Win 1382 / Loss 1488 / Flat 1664) / skip 4580件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $691.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3991件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0468 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1913件 (Win 561 / Loss 728 / Flat 624) / pending 0件 / skip 2114件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-25T00:11:15.717577+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78941.6
- Funnel: target 1022 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +89.17% | $3,511,936.39 |
| STORJ/USDT:USDT | +21.65% | $5,014,964.75 |
| ONG/USDT:USDT | +13.02% | $2,495,156.26 |
| CASHCAT/USDT:USDT | +12.74% | $2,478,291.13 |
| SCRT/USDT:USDT | +7.45% | $1,085,065.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +1.89% | +1.90% |
| ONG/USDT:USDT | below_1h_threshold | +1.40% | +1.41% |
| TUT/USDT:USDT | below_1h_threshold | +1.25% | +1.26% |
| CHIP/USDT:USDT | below_1h_threshold | +1.24% | +1.25% |
| JUP/USDT:USDT | below_1h_threshold | +1.19% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
