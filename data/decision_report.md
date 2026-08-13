# Decision Report

- generated_at: 2026-08-13T00:41:24.123610+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11411**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11411, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/19 | 10.5% | +8.00% | **+0.84%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.43% | **+0.79%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.64% | **+0.51%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.05** / 初期 $100.00 (+503.05%)
- 確定: 3950件 (Win 1232 / Loss 1292 / Flat 1426) / skip 4022件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$146.89** / 初期 $100.00 (+46.89%)
- 確定: 1600件 (Win 450 / Loss 375 / Flat 775) / skip 3222件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0849 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $146.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.00** / 初期 $100.00 (+15.00%)
- 確定: 1419件 (Win 416 / Loss 535 / Flat 468) / pending 1件 / skip 1459件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000099 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $115.00

## 6. Latest Market Context

- 更新: 2026-08-13T00:41:12.972673+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=63540.9
- Funnel: target 972 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +33.78% | $12,178,426.02 |
| COTI/USDT:USDT | +32.69% | $7,233,270.46 |
| BTW/USDT:USDT | +15.16% | $21,953,131.27 |
| VELVET/USDT:USDT | +11.20% | $20,739,246.54 |
| BANK/USDT:USDT | +9.10% | $3,185,093.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +4.23% | +4.09% |
| JTO/USDT:USDT | below_1h_threshold | +3.51% | +3.37% |
| VELVET/USDT:USDT | below_1h_threshold | +2.65% | +2.51% |
| LSK/USDT:USDT | below_1h_threshold | +2.54% | +2.41% |
| COTI/USDT:USDT | below_1h_threshold | +1.95% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
