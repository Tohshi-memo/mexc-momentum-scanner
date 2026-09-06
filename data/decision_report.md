# Decision Report

- generated_at: 2026-09-06T22:51:22.280301+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13846**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13846, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.40% | **-1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 9/20 | 45.0% | +4.86% | **+2.19%** |
| LIMIT_9PCT | 8/20 | 40.0% | +4.57% | **+1.83%** |
| LIMIT_7PCT | 10/20 | 50.0% | +2.84% | **+1.42%** |
| LIMIT_6PCT | 11/20 | 55.0% | +0.86% | **+0.47%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.27% | **+0.83%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.57% | **+0.45%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5127件 (Win 1538 / Loss 1680 / Flat 1909) / skip 5280件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4687件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0451 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.00** / 初期 $100.00 (+19.00%)
- 確定: 2440件 (Win 726 / Loss 932 / Flat 782) / pending 5件 / skip 2874件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_8PCT` TP_HIT account +0.34% 残高後 $119.00

## 6. Latest Market Context

- 更新: 2026-09-06T22:51:12.554093+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79969.9
- Funnel: target 1059 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +194.39% | $2,965,667.34 |
| TIA/USDT:USDT | +10.88% | $11,583,401.49 |
| XAN/USDT:USDT | +10.20% | $1,417,299.35 |
| LINK/USDT:USDT | +6.38% | $38,365,524.44 |
| STRK/USDT:USDT | +6.27% | $1,785,041.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.54% | +3.46% |
| STRK/USDT:USDT | below_1h_threshold | +3.32% | +3.24% |
| UAI/USDT:USDT | below_1h_threshold | +1.26% | +1.18% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.15% | +1.07% |
| LINK/USDT:USDT | below_1h_threshold | +0.94% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
