# Decision Report

- generated_at: 2026-08-16T09:16:20.835670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11729**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11729, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.61% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.71% | **+1.63%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.21% | **+1.55%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.18% | **+1.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.25% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4107件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.89** / 初期 $100.00 (+54.89%)
- 確定: 1780件 (Win 495 / Loss 417 / Flat 868) / skip 3360件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0043 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1632件 (Win 495 / Loss 618 / Flat 519) / pending 6件 / skip 1566件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000100 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T09:16:12.451542+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63039.5
- Funnel: target 986 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +28.03% | $8,134,697.94 |
| VELVET/USDT:USDT | +25.71% | $26,783,588.25 |
| AIO/USDT:USDT | +25.52% | $3,603,589.62 |
| SPORTFUN/USDT:USDT | +20.80% | $4,609,015.24 |
| H/USDT:USDT | +20.07% | $9,520,226.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIO/USDT:USDT | below_1h_threshold | +3.61% | +3.61% |
| RON/USDT:USDT | below_1h_threshold | +3.42% | +3.42% |
| VELVET/USDT:USDT | below_1h_threshold | +2.57% | +2.57% |
| HEMI/USDT:USDT | below_1h_threshold | +2.05% | +2.05% |
| APR/USDT:USDT | below_1h_threshold | +2.05% | +2.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
