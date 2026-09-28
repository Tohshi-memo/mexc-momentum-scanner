# Decision Report

- generated_at: 2026-09-28T12:46:45.243850+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15719**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15719, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/14 | 28.6% | +2.76% | **+0.79%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.80% | **+0.44%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.32% | **+0.03%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.17% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.39% | **+1.20%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.58% | **+0.92%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.69% | **+0.81%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6298件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5596件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0361 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.07** / 初期 $100.00 (+19.07%)
- 確定: 3285件 (Win 953 / Loss 1288 / Flat 1044) / pending 6件 / skip 3903件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000135 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.07

## 6. Latest Market Context

- 更新: 2026-09-28T12:46:23.641580+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=83374.9
- Funnel: target 1064 → liquid 159 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +31.29% | $1,521,566.31 |
| QNT/USDT:USDT | +29.33% | $325,771,013.22 |
| HBAR/USDT:USDT | +28.88% | $86,277,091.53 |
| MARSCOIN/USDT:USDT | +27.68% | $2,928,728.28 |
| GRT/USDT:USDT | +15.37% | $13,426,232.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +4.60% | +4.22% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +4.47% | +4.09% |
| LINK/USDT:USDT | below_1h_threshold | +4.07% | +3.68% |
| MONAD/USDT:USDT | below_1h_threshold | +3.11% | +2.73% |
| STRK/USDT:USDT | below_1h_threshold | +2.96% | +2.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
