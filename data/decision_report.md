# Decision Report

- generated_at: 2026-11-20T00:51:31.269494+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19227**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19227, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.37% | **+0.62%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.33% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.31% | **+0.65%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.45%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.24% | **+0.43%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,692.91** / 初期 $100.00 (+1592.91%)
- 確定: 7385件 (Win 2121 / Loss 2378 / Flat 2886) / skip 8403件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIPPIN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,692.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.03** / 初期 $100.00 (+339.03%)
- 確定: 5051件 (Win 1347 / Loss 1087 / Flat 2617) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $439.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7385件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000079 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T00:51:19.548901+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=62003.1
- Funnel: target 1084 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +25.36% | $2,988,770.28 |
| SOXS/USDT:USDT | +16.96% | $49,213,277.95 |
| HUMA/USDT:USDT | +14.70% | $1,398,084.71 |
| UVXY/USDT:USDT | +14.50% | $2,893,693.37 |
| SKY/USDT:USDT | +12.16% | $4,848,025.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RARE/USDT:USDT | below_1h_threshold | +4.36% | +4.29% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.88% | +2.81% |
| IRYS/USDT:USDT | below_1h_threshold | +2.38% | +2.31% |
| SOXS/USDT:USDT | below_1h_threshold | +1.68% | +1.61% |
| HUMA/USDT:USDT | below_1h_threshold | +1.01% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
