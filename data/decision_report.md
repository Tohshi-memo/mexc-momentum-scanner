# Decision Report

- generated_at: 2026-09-13T12:41:32.315030+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14431**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14431, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 19/20 | 95.0% | +1.22% | **+1.16%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.53% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.91% | **+2.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.38% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5432件 (Win 1635 / Loss 1760 / Flat 2037) / skip 5560件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.48** / 初期 $100.00 (+129.48%)
- 確定: 2949件 (Win 821 / Loss 701 / Flat 1427) / skip 4893件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0718 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $229.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.16** / 初期 $100.00 (+27.16%)
- 確定: 2854件 (Win 850 / Loss 1103 / Flat 901) / pending 2件 / skip 3049件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000438 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FLOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $127.16

## 6. Latest Market Context

- 更新: 2026-09-13T12:41:19.213027+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=76724.4
- Funnel: target 1068 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.2 >= 65=1, 4h RSI 90.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +277.04% | $102,768,249.69 |
| STEEM/USDT:USDT | +45.21% | $2,199,214.54 |
| ARK/USDT:USDT | +40.52% | $2,217,288.14 |
| BTW/USDT:USDT | +32.06% | $4,353,128.28 |
| VTHO/USDT:USDT | +30.59% | $3,339,851.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| REZ/USDT:USDT | below_1h_threshold | +3.34% | +3.36% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.70% | +1.73% |
| AAVE/USDT:USDT | below_1h_threshold | +1.14% | +1.17% |
| PI/USDT:USDT | below_1h_threshold | +1.13% | +1.15% |
| SOXS/USDT:USDT | below_1h_threshold | +0.84% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
