# Decision Report

- generated_at: 2026-09-05T14:26:22.762529+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13738**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13738, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.20% | **+0.16%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.03% | **+0.02%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.75% | **+2.06%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.26% | **+1.47%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.40** / 初期 $100.00 (+757.40%)
- 確定: 5044件 (Win 1519 / Loss 1649 / Flat 1876) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $857.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.40** / 初期 $100.00 (+88.40%)
- 確定: 2483件 (Win 696 / Loss 587 / Flat 1200) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0737 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.92** / 初期 $100.00 (+18.92%)
- 確定: 2363件 (Win 703 / Loss 901 / Flat 759) / pending 2件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.92

## 6. Latest Market Context

- 更新: 2026-09-05T14:26:13.424552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79637.6
- Funnel: target 1050 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +77.04% | $15,494,997.21 |
| 4/USDT:USDT | +66.56% | $21,697,509.84 |
| BASECAT/USDT:USDT | +41.82% | $1,874,539.42 |
| AKE/USDT:USDT | +41.79% | $19,210,269.18 |
| ICX/USDT:USDT | +38.43% | $1,114,305.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.71% | +3.63% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.78% | +2.70% |
| CHIP/USDT:USDT | below_1h_threshold | +1.42% | +1.34% |
| ICX/USDT:USDT | below_1h_threshold | +1.38% | +1.30% |
| AR/USDT:USDT | below_1h_threshold | +1.36% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
