# Decision Report

- generated_at: 2026-06-08T17:55:09.140666+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6093**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6093, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.46% | **-1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.39% | **+0.16%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT | 19/20 | 95.0% | -0.26% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| ASK_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.80% | **+1.17%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.48% | **+1.06%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1510件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T17:55:01.849449+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63476.0
- Funnel: target 777 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +38.20% | $17,997,760.42 |
| PIPPIN/USDT:USDT | +18.65% | $23,615,112.60 |
| LAYER/USDT:USDT | +14.76% | $1,272,192.66 |
| WLD/USDT:USDT | +11.06% | $99,532,380.67 |
| BLESS/USDT:USDT | +8.32% | $10,399,176.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +4.98% | +5.01% |
| SIREN/USDT:USDT | below_1h_threshold | +4.09% | +4.12% |
| INJ/USDT:USDT | below_1h_threshold | +2.36% | +2.40% |
| MOVE/USDT:USDT | below_1h_threshold | +2.28% | +2.31% |
| CHIP/USDT:USDT | below_1h_threshold | +2.19% | +2.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
