# Decision Report

- generated_at: 2026-08-25T05:51:23.533371+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12582**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12582, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/14 | 42.9% | +1.11% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.47% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.74% | **+0.96%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.46% | **+0.88%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.71% | **+0.46%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$705.64** / 初期 $100.00 (+605.64%)
- 確定: 4562件 (Win 1389 / Loss 1495 / Flat 1678) / skip 4581件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $705.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4016件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0171 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.17** / 初期 $100.00 (+15.17%)
- 確定: 1915件 (Win 561 / Loss 729 / Flat 625) / pending 1件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.17

## 6. Latest Market Context

- 更新: 2026-08-25T05:51:13.332000+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.46% price=80720.0
- Funnel: target 1028 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +70.24% | $4,250,449.28 |
| TAC/USDT:USDT | +48.70% | $3,755,036.74 |
| CASHCAT/USDT:USDT | +26.11% | $2,755,310.83 |
| PONS/USDT:USDT | +21.75% | $1,520,377.52 |
| BR/USDT:USDT | +19.83% | $1,519,141.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STX/USDT:USDT | below_1h_threshold | +4.99% | +4.52% |
| US/USDT:USDT | below_1h_threshold | +4.51% | +4.05% |
| TAC/USDT:USDT | below_1h_threshold | +3.54% | +3.07% |
| WIF/USDT:USDT | below_1h_threshold | +3.25% | +2.79% |
| BR/USDT:USDT | below_1h_threshold | +3.23% | +2.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
