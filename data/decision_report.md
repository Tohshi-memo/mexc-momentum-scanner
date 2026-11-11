# Decision Report

- generated_at: 2026-11-11T16:21:32.932033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18691**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18691, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +1.00% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.25% | **+0.38%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.26% | **+0.22%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.62% | **+1.97%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.96% | **+1.48%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +3.56% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定トレード: 270件 (TP 97 / SL 165 / EXP 8)
- 最新: SNXX/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,704.29** / 初期 $100.00 (+1604.29%)
- 確定: 7223件 (Win 2079 / Loss 2310 / Flat 2834) / skip 8029件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,704.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4778件 (Win 1283 / Loss 1056 / Flat 2439) / skip 7324件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0894 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6851件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T16:21:17.067311+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=74196.5
- Funnel: target 1103 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEC/USDT:USDT | +1.98% | $2,044,407,291.59 |
| ZRO/USDT:USDT | +1.81% | $2,555,979.03 |
| PIEVERSE/USDT:USDT | +1.73% | $3,096,744.22 |
| USELESS/USDT:USDT | +1.43% | $3,978,661.50 |
| ETHFI/USDT:USDT | +1.28% | $3,745,750.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.15% | +2.83% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.02% | +1.69% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +1.68% |
| ZEC/USDT:USDT | below_1h_threshold | +1.99% | +1.66% |
| ZRO/USDT:USDT | below_1h_threshold | +1.82% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
