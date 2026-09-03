# Decision Report

- generated_at: 2026-09-03T07:36:18.025057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13453**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13453, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.90% | **-0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.31% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.70% | **+2.96%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.08% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.48% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5006件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2372件 (Win 671 / Loss 576 / Flat 1125) / skip 4492件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0422 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.23** / 初期 $100.00 (+14.23%)
- 確定: 2149件 (Win 632 / Loss 843 / Flat 674) / pending 5件 / skip 2773件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $114.23

## 6. Latest Market Context

- 更新: 2026-09-03T07:36:08.357200+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77879.7
- Funnel: target 1046 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +83.87% | $5,255,215.25 |
| EDGE/USDT:USDT | +35.93% | $2,811,391.92 |
| HEMI/USDT:USDT | +32.06% | $3,514,425.86 |
| USELESS/USDT:USDT | +28.13% | $24,072,492.29 |
| BR/USDT:USDT | +26.23% | $1,028,064.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +3.40% | +3.29% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.89% | +2.78% |
| APT/USDT:USDT | below_1h_threshold | +2.88% | +2.77% |
| CHIP/USDT:USDT | below_1h_threshold | +2.03% | +1.92% |
| BONER/USDT:USDT | below_1h_threshold | +1.48% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
