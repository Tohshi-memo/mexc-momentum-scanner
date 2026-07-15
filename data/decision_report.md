# Decision Report

- generated_at: 2026-07-15T10:36:17.989298+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8735**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8735, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 10/20 | 50.0% | +4.04% | **+2.02%** |
| LIMIT_8PCT | 9/20 | 45.0% | +4.38% | **+1.97%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.34% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.71% | **+3.15%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.75% | **+3.00%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +4.07% | **+2.44%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.76% | **+1.79%** |

## 2. $100 Live Portfolio

- 残高: **$102.71** / 初期 $100.00 (+2.71%)
- 確定トレード: 97件 (TP 33 / SL 62 / EXP 2)
- 最新: DODO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.63** / 初期 $100.00 (+242.63%)
- 確定: 2879件 (Win 901 / Loss 935 / Flat 1043) / skip 2417件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.82% 残高後 $342.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.99** / 初期 $100.00 (+5.99%)
- 確定: 703件 (Win 164 / Loss 165 / Flat 374) / skip 1443件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0920 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $105.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 1件 / skip 149件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000326 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T10:36:11.813860+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=64585.4
- Funnel: target 867 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +195.27% | $16,113,043.27 |
| DODO/USDT:USDT | +38.37% | $10,119,154.40 |
| AEHRSTOCK/USDT:USDT | +30.22% | $3,812,139.30 |
| US/USDT:USDT | +29.77% | $4,530,640.13 |
| MAGMA/USDT:USDT | +19.37% | $2,295,133.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XEC/USDT:USDT | below_1h_threshold | +4.89% | +4.98% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.51% | +3.60% |
| 2Z/USDT:USDT | below_1h_threshold | +1.43% | +1.53% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.27% | +1.36% |
| TIA/USDT:USDT | below_1h_threshold | +1.13% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
