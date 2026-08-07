# Decision Report

- generated_at: 2026-08-07T16:36:36.962702+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10731**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=10731, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.19% | **+0.72%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.60% | **+0.48%** |
| LIMIT_BB3S | 7/20 | 35.0% | +1.27% | **+0.45%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.68% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.17% | **+0.41%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.84% | **-0.33%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.59% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3799件 (Win 1203 / Loss 1250 / Flat 1346) / skip 3493件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1457件 (Win 407 / Loss 342 / Flat 708) / skip 2685件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.65** / 初期 $100.00 (+18.65%)
- 確定: 1176件 (Win 380 / Loss 463 / Flat 333) / pending 6件 / skip 1028件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.65

## 6. Latest Market Context

- 更新: 2026-08-07T16:36:22.880088+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64940.5
- Funnel: target 961 → liquid 192 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1, 4h RSI 92.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +12.47% | $26,253,216.79 |
| CYS/USDT:USDT | +10.15% | $13,230,739.02 |
| EPIC/USDT:USDT | +7.19% | $1,630,769.10 |
| BICO/USDT:USDT | +5.88% | $34,578,784.70 |
| MMT/USDT:USDT | +5.47% | $1,037,690.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_relative_strength | +5.04% | +4.95% |
| KGEN/USDT:USDT | below_1h_threshold | +3.74% | +3.65% |
| C98/USDT:USDT | below_1h_threshold | +3.52% | +3.44% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +3.45% | +3.37% |
| CC/USDT:USDT | below_1h_threshold | +2.57% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
