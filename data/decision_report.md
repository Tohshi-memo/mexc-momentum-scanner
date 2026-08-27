# Decision Report

- generated_at: 2026-08-27T07:36:15.884480+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12794**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12794, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/16 | 56.2% | +2.24% | **+1.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.58% | **+0.29%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.27% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.27% | **+1.36%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.00% | **+0.90%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.00% | **+0.80%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.95% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.03** / 初期 $100.00 (+616.03%)
- 確定: 4669件 (Win 1414 / Loss 1532 / Flat 1723) / skip 4686件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2002件 (Win 544 / Loss 483 / Flat 975) / skip 4203件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0708 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1984件 (Win 580 / Loss 758 / Flat 646) / pending 0件 / skip 2283件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-27T07:36:06.699777+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78829.9
- Funnel: target 1018 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +43.22% | $3,889,496.49 |
| TAC/USDT:USDT | +28.47% | $13,261,112.08 |
| RUNE/USDT:USDT | +27.53% | $2,014,987.12 |
| VET/USDT:USDT | +19.03% | $2,333,936.84 |
| BTR/USDT:USDT | +18.74% | $23,452,806.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.60% | +2.58% |
| TAO/USDT:USDT | below_1h_threshold | +1.96% | +1.94% |
| VET/USDT:USDT | below_1h_threshold | +1.65% | +1.62% |
| ZRO/USDT:USDT | below_1h_threshold | +1.51% | +1.48% |
| CYS/USDT:USDT | below_1h_threshold | +1.45% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
