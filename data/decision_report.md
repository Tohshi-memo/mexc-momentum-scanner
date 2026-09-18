# Decision Report

- generated_at: 2026-09-18T10:51:29.174356+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14887**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14887, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.30% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.13% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +1.01% | **+0.76%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,153.97** / 初期 $100.00 (+1053.97%)
- 確定: 5605件 (Win 1679 / Loss 1815 / Flat 2111) / skip 5843件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,153.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.67** / 初期 $100.00 (+141.67%)
- 確定: 3173件 (Win 878 / Loss 757 / Flat 1538) / skip 5125件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0732 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $241.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.32** / 初期 $100.00 (+23.32%)
- 確定: 2960件 (Win 878 / Loss 1166 / Flat 916) / pending 0件 / skip 3403件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.32

## 6. Latest Market Context

- 更新: 2026-09-18T10:51:17.260519+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=78289.3
- Funnel: target 1050 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.4 >= 65=1, 4h RSI 92.4 >= 65=1, 4h RSI 76.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| G/USDT:USDT | +62.48% | $13,144,189.34 |
| CNPY/USDT:USDT | +39.15% | $3,949,001.45 |
| ONE/USDT:USDT | +28.51% | $54,309,074.76 |
| UNI/USDT:USDT | +27.96% | $89,076,058.35 |
| NEAR/USDT:USDT | +24.18% | $147,403,238.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.51% | +3.35% |
| KAS/USDT:USDT | below_1h_threshold | +2.37% | +2.22% |
| CNPY/USDT:USDT | below_1h_threshold | +2.19% | +2.03% |
| LIT/USDT:USDT | below_1h_threshold | +1.98% | +1.82% |
| HYPE/USDT:USDT | below_1h_threshold | +1.97% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
