# Decision Report

- generated_at: 2026-09-07T07:41:23.845059+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13870**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13870, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.51% | **+0.25%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.58% | **+0.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.09% | **+1.68%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.70% | **+1.61%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.08% | **+1.46%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.29% | **+0.65%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.99% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$840.73** / 初期 $100.00 (+740.73%)
- 確定: 5143件 (Win 1540 / Loss 1681 / Flat 1922) / skip 5288件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $840.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4710件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0648 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.20** / 初期 $100.00 (+19.20%)
- 確定: 2462件 (Win 730 / Loss 936 / Flat 796) / pending 3件 / skip 2875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000278 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $119.20

## 6. Latest Market Context

- 更新: 2026-09-07T07:41:11.858163+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.62% price=79126.3
- Funnel: target 1059 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +294.01% | $1,578,840.55 |
| BONER/USDT:USDT | +124.16% | $5,171,930.87 |
| XAN/USDT:USDT | +12.22% | $2,316,105.81 |
| ICP/USDT:USDT | +11.36% | $9,955,168.77 |
| BULLA/USDT:USDT | +10.80% | $7,122,754.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +2.78% | +3.40% |
| AKE/USDT:USDT | below_1h_threshold | +2.48% | +3.09% |
| ICP/USDT:USDT | below_1h_threshold | +1.60% | +2.22% |
| WLD/USDT:USDT | below_1h_threshold | +1.44% | +2.06% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.79% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
