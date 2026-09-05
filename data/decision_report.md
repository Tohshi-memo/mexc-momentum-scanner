# Decision Report

- generated_at: 2026-09-05T12:16:21.816190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13730**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13730, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.99% | **+0.79%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.37% | **+1.90%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.87% | **+1.58%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.37% | **+1.07%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.46** / 初期 $100.00 (+757.46%)
- 確定: 5036件 (Win 1518 / Loss 1647 / Flat 1871) / skip 5255件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.90% 残高後 $857.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.12** / 初期 $100.00 (+88.12%)
- 確定: 2475件 (Win 695 / Loss 587 / Flat 1193) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0642 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.78** / 初期 $100.00 (+18.78%)
- 確定: 2355件 (Win 702 / Loss 901 / Flat 752) / pending 4件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.78

## 6. Latest Market Context

- 更新: 2026-09-05T12:16:11.680454+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=79622.1
- Funnel: target 1050 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +81.91% | $13,803,575.32 |
| 4/USDT:USDT | +57.33% | $20,269,570.46 |
| BASECAT/USDT:USDT | +43.25% | $1,782,982.84 |
| AKE/USDT:USDT | +42.83% | $16,760,469.69 |
| NIULAI/USDT:USDT | +41.06% | $1,698,594.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +5.00% | +4.94% |
| BULLA/USDT:USDT | below_1h_threshold | +4.47% | +4.41% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.77% | +2.71% |
| CAKE/USDT:USDT | below_1h_threshold | +2.61% | +2.55% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.02% | +1.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
