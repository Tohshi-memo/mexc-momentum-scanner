# Decision Report

- generated_at: 2026-08-25T03:11:22.634753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12570**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12570, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.30% | **+0.81%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_BB3S | 3/17 | 17.6% | +3.54% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.73% | **+1.23%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.49% | **+0.97%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.70% | **+0.94%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.52% | **+0.83%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$688.38** / 初期 $100.00 (+588.38%)
- 確定: 4550件 (Win 1385 / Loss 1492 / Flat 1673) / skip 4581件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $688.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4004件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0453 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1913件 (Win 561 / Loss 728 / Flat 624) / pending 0件 / skip 2129件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000177 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-25T03:11:13.705390+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=80818.3
- Funnel: target 1022 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +73.96% | $4,130,842.30 |
| TAC/USDT:USDT | +44.75% | $2,477,966.66 |
| CASHCAT/USDT:USDT | +21.96% | $2,650,337.20 |
| ONG/USDT:USDT | +17.72% | $3,339,257.54 |
| STORJ/USDT:USDT | +17.19% | $5,131,930.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.30% | +4.06% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.33% | +3.10% |
| PEPE/USDT:USDT | below_1h_threshold | +1.84% | +1.61% |
| PROM/USDT:USDT | below_1h_threshold | +1.42% | +1.19% |
| ONG/USDT:USDT | below_1h_threshold | +0.96% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
