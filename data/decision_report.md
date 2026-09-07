# Decision Report

- generated_at: 2026-09-07T22:51:21.216696+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13920**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13920, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.85% | **-2.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +4.66% | **+3.73%** |
| MARKET_LONG | 20/20 | 100.0% | +3.59% | **+3.59%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +5.22% | **+2.61%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +4.35% | **+1.52%** |
| LIMIT_7PCT_LONG | 2/20 | 10.0% | +4.09% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$963.62** / 初期 $100.00 (+863.62%)
- 確定: 5193件 (Win 1560 / Loss 1684 / Flat 1949) / skip 5288件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $963.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4759件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0266 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.39** / 初期 $100.00 (+22.39%)
- 確定: 2510件 (Win 741 / Loss 940 / Flat 829) / pending 6件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000430 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $122.39

## 6. Latest Market Context

- 更新: 2026-09-07T22:51:07.270272+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=78915.0
- Funnel: target 1062 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +56.04% | $5,850,333.32 |
| BONER/USDT:USDT | +19.23% | $5,635,563.98 |
| SOPH/USDT:USDT | +15.91% | $1,736,728.72 |
| AERO/USDT:USDT | +10.87% | $3,701,773.77 |
| INJ/USDT:USDT | +7.31% | $43,244,677.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +3.57% | +3.84% |
| XAN/USDT:USDT | below_1h_threshold | +3.16% | +3.43% |
| SOPH/USDT:USDT | below_1h_threshold | +2.80% | +3.07% |
| UAI/USDT:USDT | below_1h_threshold | +1.58% | +1.85% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.36% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
