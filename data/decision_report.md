# Decision Report

- generated_at: 2026-07-07T17:17:48.844175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8447**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8447, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.94% | **+0.73%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S | 5/14 | 35.7% | -0.21% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.96% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$100.55** / 初期 $100.00 (+0.55%)
- 確定トレード: 69件 (TP 23 / SL 45 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.55
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.09** / 初期 $100.00 (+222.09%)
- 確定: 2652件 (Win 845 / Loss 896 / Flat 911) / skip 2356件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $322.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 640件 (Win 152 / Loss 158 / Flat 330) / skip 1218件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0209 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T17:17:42.435886+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63900.1
- Funnel: target 847 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +26.97% | $25,202,542.88 |
| EDGE/USDT:USDT | +13.24% | $9,458,763.47 |
| USELESS/USDT:USDT | +4.48% | $1,666,609.81 |
| BTW/USDT:USDT | +4.23% | $1,094,217.40 |
| SOXL/USDT:USDT | +3.93% | $18,951,975.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| YFI/USDT:USDT | below_1h_threshold | +2.21% | +2.30% |
| SYN/USDT:USDT | below_1h_threshold | +2.11% | +2.21% |
| ALLO/USDT:USDT | below_1h_threshold | +1.37% | +1.47% |
| DEXE/USDT:USDT | below_1h_threshold | +1.36% | +1.45% |
| BTW/USDT:USDT | below_1h_threshold | +1.10% | +1.20% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
