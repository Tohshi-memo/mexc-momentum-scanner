# Decision Report

- generated_at: 2026-11-06T17:06:09.784086+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18311**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18311, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.28% | **+0.64%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.91% | **+1.02%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.42% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7837件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$387.52** / 初期 $100.00 (+287.52%)
- 確定: 4681件 (Win 1258 / Loss 1037 / Flat 2386) / skip 7041件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0410 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $387.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6477件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T17:06:01.520249+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=75921.0
- Funnel: target 1089 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +11.60% | $4,470,880.98 |
| LYN/USDT:USDT | +8.92% | $1,629,786.21 |
| BTW/USDT:USDT | +7.94% | $8,395,487.04 |
| AKE/USDT:USDT | +4.83% | $54,086,248.48 |
| UAI/USDT:USDT | +4.68% | $22,172,645.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRNASTOCK/USDT:USDT | below_1h_threshold | +2.61% | +2.69% |
| MUU/USDT:USDT | below_1h_threshold | +2.18% | +2.25% |
| IDOL/USDT:USDT | below_1h_threshold | +1.83% | +1.91% |
| ICNT/USDT:USDT | below_1h_threshold | +1.80% | +1.88% |
| ONE/USDT:USDT | below_1h_threshold | +1.77% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
