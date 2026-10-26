# Decision Report

- generated_at: 2026-10-26T23:36:26.603238+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17535**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17535, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +5.67% | **+1.99%** |
| LIMIT_BB3S | 10/17 | 58.8% | +3.10% | **+1.82%** |
| LIMIT_ATR | 16/20 | 80.0% | +2.20% | **+1.76%** |
| LIMIT_9PCT | 5/20 | 25.0% | +4.92% | **+1.23%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.94% | **+3.94%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.89% | **+2.17%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.37% | **+2.02%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.69% | **+1.60%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.71% | **+1.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7375件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$322.69** / 初期 $100.00 (+222.69%)
- 確定: 4064件 (Win 1120 / Loss 955 / Flat 1989) / skip 6882件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0789 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRENSTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $322.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5693件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000363 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T23:36:11.625297+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=80117.6
- Funnel: target 1078 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +237.40% | $22,246,158.07 |
| US/USDT:USDT | +26.06% | $1,046,821.36 |
| AGT/USDT:USDT | +6.93% | $1,717,327.85 |
| DODO/USDT:USDT | +5.95% | $1,071,389.55 |
| DNA/USDT:USDT | +5.24% | $1,208,589.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +1.50% | +1.33% |
| BAT/USDT:USDT | below_1h_threshold | +1.42% | +1.25% |
| STRK/USDT:USDT | below_1h_threshold | +1.27% | +1.10% |
| UNI/USDT:USDT | below_1h_threshold | +1.06% | +0.88% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.98% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
