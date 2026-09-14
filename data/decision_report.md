# Decision Report

- generated_at: 2026-09-14T02:36:31.425460+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14480**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14480, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.42% | **+1.35%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.42% | **+1.20%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.23% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.41% | **+0.19%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.66** / 初期 $100.00 (+972.66%)
- 確定: 5434件 (Win 1635 / Loss 1762 / Flat 2037) / skip 5607件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.22% 残高後 $1,072.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4900件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0630 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.60** / 初期 $100.00 (+26.60%)
- 確定: 2865件 (Win 852 / Loss 1109 / Flat 904) / pending 3件 / skip 3083件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.60

## 6. Latest Market Context

- 更新: 2026-09-14T02:36:16.134767+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=77565.1
- Funnel: target 1068 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +54.57% | $1,351,981.70 |
| POWER/USDT:USDT | +20.14% | $4,871,338.77 |
| BR/USDT:USDT | +12.22% | $2,440,095.34 |
| ARK/USDT:USDT | +11.93% | $3,119,141.00 |
| MAGMA/USDT:USDT | +8.31% | $1,814,112.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_relative_strength | +5.23% | +4.62% |
| LIT/USDT:USDT | below_1h_threshold | +4.60% | +3.99% |
| BTW/USDT:USDT | below_1h_threshold | +3.61% | +2.99% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.69% | +2.08% |
| AR/USDT:USDT | below_1h_threshold | +2.56% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
