# Decision Report

- generated_at: 2026-08-07T10:51:44.130645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10702, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +2.33% | **+1.16%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_BB3S | 2/15 | 13.3% | +1.87% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.44% | **+2.23%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.28% | **+1.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.80% | **+1.12%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.03% | **+1.06%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.94% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3465件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1455件 (Win 407 / Loss 342 / Flat 706) / skip 2658件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.47** / 初期 $100.00 (+16.47%)
- 確定: 1160件 (Win 371 / Loss 456 / Flat 333) / pending 1件 / skip 1017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.47

## 6. Latest Market Context

- 更新: 2026-08-07T10:51:28.024384+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64873.1
- Funnel: target 961 → liquid 190 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.3 >= 65=1, 4h RSI 90.9 >= 65=1, 4h RSI 87.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +35.44% | $25,716,935.76 |
| SKYAI/USDT:USDT | +30.98% | $70,438,453.28 |
| CATE/USDT:USDT | +30.04% | $4,394,029.11 |
| EPIC/USDT:USDT | +24.17% | $1,055,693.64 |
| ON/USDT:USDT | +23.40% | $11,834,754.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KMNO/USDT:USDT | below_1h_threshold | +2.65% | +2.55% |
| TAKE/USDT:USDT | below_1h_threshold | +2.42% | +2.32% |
| ALLO/USDT:USDT | below_1h_threshold | +2.06% | +1.96% |
| ON/USDT:USDT | below_1h_threshold | +1.84% | +1.74% |
| ACE/USDT:USDT | below_1h_threshold | +1.82% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
