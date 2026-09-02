# Decision Report

- generated_at: 2026-09-02T02:16:27.441327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13285**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13285, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.85% | **+1.16%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.83% | **+0.42%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.27% | **+2.56%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.80% | **+1.90%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.71% | **+1.41%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.76% | **+1.14%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.26% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$832.07** / 初期 $100.00 (+732.07%)
- 確定: 4920件 (Win 1499 / Loss 1619 / Flat 1802) / skip 4926件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $832.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.22** / 初期 $100.00 (+75.22%)
- 確定: 2264件 (Win 634 / Loss 544 / Flat 1086) / skip 4432件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $175.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2667件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T02:16:16.103954+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=77104.4
- Funnel: target 1036 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +29.02% | $17,599,365.93 |
| MAGMA/USDT:USDT | +26.49% | $4,898,002.12 |
| ACE/USDT:USDT | +14.32% | $11,183,277.69 |
| BONER/USDT:USDT | +12.63% | $2,492,226.05 |
| HEMI/USDT:USDT | +10.68% | $5,331,998.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.67% | +3.52% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.51% | +2.35% |
| BEAT/USDT:USDT | below_1h_threshold | +2.36% | +2.21% |
| AKE/USDT:USDT | below_1h_threshold | +1.18% | +1.03% |
| CRV/USDT:USDT | below_1h_threshold | +1.11% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
