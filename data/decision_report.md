# Decision Report

- generated_at: 2026-09-09T06:21:23.407892+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14038**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14038, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.04% | **+0.83%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.82% | **+0.70%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.99% | **+0.69%** |
| LIMIT_BB3S | 3/16 | 18.8% | +3.52% | **+0.66%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.02% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,012.11** / 初期 $100.00 (+912.11%)
- 確定: 5302件 (Win 1591 / Loss 1708 / Flat 2003) / skip 5297件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,012.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.12** / 初期 $100.00 (+90.12%)
- 確定: 2641件 (Win 727 / Loss 623 / Flat 1291) / skip 4808件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.81** / 初期 $100.00 (+17.81%)
- 確定: 2618件 (Win 764 / Loss 1000 / Flat 854) / pending 2件 / skip 2889件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.81

## 6. Latest Market Context

- 更新: 2026-09-09T06:21:13.104024+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=79146.1
- Funnel: target 1070 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +74.09% | $1,109,662.35 |
| OL/USDT:USDT | +24.06% | $2,138,238.29 |
| NIULAI/USDT:USDT | +21.88% | $1,367,713.70 |
| IOST/USDT:USDT | +20.47% | $2,431,930.78 |
| WAVES/USDT:USDT | +17.23% | $1,622,455.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IOST/USDT:USDT | below_1h_threshold | +3.71% | +3.41% |
| ARB/USDT:USDT | below_1h_threshold | +2.95% | +2.65% |
| ZEC/USDT:USDT | below_1h_threshold | +1.59% | +1.29% |
| MONAD/USDT:USDT | below_1h_threshold | +1.51% | +1.20% |
| ENA/USDT:USDT | below_1h_threshold | +1.50% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
