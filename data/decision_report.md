# Decision Report

- generated_at: 2026-10-27T00:41:25.947173+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17539**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17539, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +5.06% | **+1.77%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_ATR | 17/20 | 85.0% | +1.08% | **+0.92%** |
| LIMIT_BB3S | 9/17 | 52.9% | +1.72% | **+0.91%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.94% | **+3.94%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.93% | **+2.75%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.79% | **+2.23%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.36% | **+2.13%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.14% | **+2.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7379件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$323.44** / 初期 $100.00 (+223.44%)
- 確定: 4068件 (Win 1121 / Loss 955 / Flat 1992) / skip 6882件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1193 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $323.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5699件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000357 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T00:41:09.054251+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=80285.8
- Funnel: target 1078 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +247.23% | $24,582,125.84 |
| IRYS/USDT:USDT | +21.93% | $9,615,747.44 |
| SYN/USDT:USDT | +18.24% | $1,209,095.73 |
| US/USDT:USDT | +15.62% | $1,235,559.83 |
| AGT/USDT:USDT | +8.81% | $1,755,597.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.23% | +4.02% |
| DNA/USDT:USDT | below_1h_threshold | +3.46% | +3.25% |
| APR/USDT:USDT | below_1h_threshold | +2.99% | +2.78% |
| NIL/USDT:USDT | below_1h_threshold | +2.92% | +2.70% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
