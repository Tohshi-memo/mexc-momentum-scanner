# Decision Report

- generated_at: 2026-11-19T19:16:37.019708+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19213**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19213, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.62% | **+0.16%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.87% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.62% | **+1.63%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.77% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,692.99** / 初期 $100.00 (+1592.99%)
- 確定: 7381件 (Win 2119 / Loss 2376 / Flat 2886) / skip 8393件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANTHROPIC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,692.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$433.12** / 初期 $100.00 (+333.12%)
- 確定: 5038件 (Win 1343 / Loss 1087 / Flat 2608) / skip 7586件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0020 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ICNT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $433.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7377件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T19:16:25.063831+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=62670.1
- Funnel: target 1084 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +14.19% | $8,797,289.59 |
| ICNT/USDT:USDT | +13.47% | $5,002,654.18 |
| SOXS/USDT:USDT | +8.83% | $48,330,598.96 |
| UVXY/USDT:USDT | +8.82% | $2,268,885.95 |
| BTW/USDT:USDT | +6.17% | $5,985,367.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +1.96% | +2.28% |
| UVXY/USDT:USDT | below_1h_threshold | +1.47% | +1.78% |
| BLESS/USDT:USDT | below_1h_threshold | +1.42% | +1.74% |
| MMT/USDT:USDT | below_1h_threshold | +1.30% | +1.61% |
| BTW/USDT:USDT | below_1h_threshold | +1.25% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
