# Decision Report

- generated_at: 2026-07-20T19:21:21.588609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9126**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9126, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_BB3S | 3/13 | 23.1% | -0.77% | **-0.18%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.72% | **+0.95%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.11% | **+0.94%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$406.94** / 初期 $100.00 (+306.94%)
- 確定: 3188件 (Win 997 / Loss 1011 / Flat 1180) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $406.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.90** / 初期 $100.00 (+27.90%)
- 確定: 1087件 (Win 283 / Loss 220 / Flat 584) / skip 1450件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1102 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $127.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.84** / 初期 $100.00 (+1.84%)
- 確定: 324件 (Win 114 / Loss 141 / Flat 69) / pending 5件 / skip 270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000332 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.84

## 6. Latest Market Context

- 更新: 2026-07-20T19:21:12.386118+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=65129.4
- Funnel: target 885 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +45.57% | $1,206,347.46 |
| ACE/USDT:USDT | +16.44% | $33,311,077.86 |
| ON/USDT:USDT | +7.14% | $1,436,522.85 |
| ANSEM/USDT:USDT | +5.63% | $2,517,288.84 |
| LDO/USDT:USDT | +5.15% | $3,133,723.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +1.67% | +1.80% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.21% | +1.34% |
| USOIL/USDT:USDT | below_1h_threshold | +0.74% | +0.87% |
| ON/USDT:USDT | below_1h_threshold | +0.70% | +0.84% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.69% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
