# Decision Report

- generated_at: 2026-08-30T07:56:17.425413+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13035**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13035, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.14% | **+0.34%** |
| LIMIT_BB3S | 11/17 | 64.7% | +0.50% | **+0.33%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_10PCT | 4/20 | 20.0% | +1.36% | **+0.27%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.93% | **+0.65%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$782.55** / 初期 $100.00 (+682.55%)
- 確定: 4805件 (Win 1463 / Loss 1582 / Flat 1760) / skip 4791件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $782.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.48** / 初期 $100.00 (+72.48%)
- 確定: 2119件 (Win 591 / Loss 517 / Flat 1011) / skip 4327件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0387 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $172.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.11** / 初期 $100.00 (+17.11%)
- 確定: 2077件 (Win 610 / Loss 806 / Flat 661) / pending 5件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.11

## 6. Latest Market Context

- 更新: 2026-08-30T07:56:07.845464+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=78100.0
- Funnel: target 1023 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +79.18% | $1,771,201.18 |
| HNT/USDT:USDT | +78.09% | $38,747,116.66 |
| NIULAI/USDT:USDT | +61.62% | $3,210,261.11 |
| FONE/USDT:USDT | +48.29% | $1,474,349.82 |
| PROM/USDT:USDT | +29.79% | $15,634,965.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FONE/USDT:USDT | below_1h_threshold | +3.78% | +3.98% |
| O/USDT:USDT | below_1h_threshold | +1.59% | +1.78% |
| UAI/USDT:USDT | below_1h_threshold | +1.54% | +1.74% |
| DOS/USDT:USDT | below_1h_threshold | +1.07% | +1.27% |
| ZKP/USDT:USDT | below_1h_threshold | +0.79% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
