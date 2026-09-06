# Decision Report

- generated_at: 2026-09-06T21:56:23.662178+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13842**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13842, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 7/20 | 35.0% | +4.08% | **+1.43%** |
| LIMIT_8PCT | 7/20 | 35.0% | +3.96% | **+1.39%** |
| LIMIT_7PCT | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.28% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5127件 (Win 1538 / Loss 1680 / Flat 1909) / skip 5276件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4683件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0322 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.64** / 初期 $100.00 (+18.64%)
- 確定: 2437件 (Win 724 / Loss 931 / Flat 782) / pending 6件 / skip 2874件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000088 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.64

## 6. Latest Market Context

- 更新: 2026-09-06T21:56:11.763780+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=79880.0
- Funnel: target 1059 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +163.77% | $2,461,682.71 |
| XAN/USDT:USDT | +10.91% | $1,270,203.35 |
| TIA/USDT:USDT | +10.07% | $10,719,222.88 |
| TAO/USDT:USDT | +7.53% | $72,701,655.53 |
| 4/USDT:USDT | +6.73% | $8,060,031.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +4.64% | +4.63% |
| TIA/USDT:USDT | below_1h_threshold | +4.26% | +4.25% |
| JTO/USDT:USDT | below_1h_threshold | +3.38% | +3.37% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.06% | +3.05% |
| KAS/USDT:USDT | below_1h_threshold | +2.94% | +2.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
