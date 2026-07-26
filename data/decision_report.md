# Decision Report

- generated_at: 2026-07-26T08:26:19.729781+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9563**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9563, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.87% | **-0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.04% | **+0.76%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.69% | **+0.58%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.88% | **+0.51%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.38% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.60% | **+1.26%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.69% | **+1.18%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.87% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$466.38** / 初期 $100.00 (+366.38%)
- 確定: 3391件 (Win 1078 / Loss 1100 / Flat 1213) / skip 2733件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $466.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.66** / 初期 $100.00 (+39.66%)
- 確定: 1216件 (Win 338 / Loss 270 / Flat 608) / skip 1758件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1347 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $139.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.43** / 初期 $100.00 (+9.43%)
- 確定: 606件 (Win 206 / Loss 231 / Flat 169) / pending 4件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000546 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $109.43

## 6. Latest Market Context

- 更新: 2026-07-26T08:26:10.502412+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64360.0
- Funnel: target 898 → liquid 119 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +68.87% | $38,502,289.13 |
| PIEVERSE/USDT:USDT | +48.67% | $3,595,793.43 |
| DIA/USDT:USDT | +40.08% | $2,214,036.83 |
| BANK/USDT:USDT | +21.14% | $93,565,033.28 |
| SHIB/USDT:USDT | +18.52% | $73,791,243.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EUL/USDT:USDT | below_1h_threshold | +3.15% | +3.12% |
| BANK/USDT:USDT | below_1h_threshold | +2.61% | +2.58% |
| DIA/USDT:USDT | below_1h_threshold | +2.27% | +2.24% |
| BEAT/USDT:USDT | below_1h_threshold | +1.76% | +1.73% |
| KAITO/USDT:USDT | below_1h_threshold | +1.70% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
