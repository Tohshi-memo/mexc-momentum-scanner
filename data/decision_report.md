# Decision Report

- generated_at: 2026-10-19T03:56:33.393490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16976**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16976, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/19 | 21.1% | +3.92% | **+0.82%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.01% | **+0.75%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.40% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.87% | **+1.22%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.17% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 245件 (TP 91 / SL 147 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,274.92** / 初期 $100.00 (+1174.92%)
- 確定: 6421件 (Win 1867 / Loss 2052 / Flat 2502) / skip 7116件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,274.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.84** / 初期 $100.00 (+176.84%)
- 確定: 3741件 (Win 1034 / Loss 881 / Flat 1826) / skip 6646件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0854 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $276.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5138件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T03:56:16.880348+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=82465.0
- Funnel: target 1084 → liquid 144 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1, 4h RSI 80.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +27.92% | $1,329,685.93 |
| Q/USDT:USDT | +23.06% | $9,774,952.74 |
| KORU/USDT:USDT | +17.43% | $42,830,349.88 |
| SNXX/USDT:USDT | +12.70% | $11,235,531.03 |
| UNITREE/USDT:USDT | +11.98% | $1,142,283.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVA/USDT:USDT | below_1h_threshold | +3.70% | +3.96% |
| BR/USDT:USDT | below_1h_threshold | +2.77% | +3.04% |
| KORU/USDT:USDT | below_1h_threshold | +2.35% | +2.61% |
| UAI/USDT:USDT | below_1h_threshold | +1.54% | +1.80% |
| SNXX/USDT:USDT | below_1h_threshold | +1.48% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
