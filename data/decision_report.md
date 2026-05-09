# Decision Report

- generated_at: 2026-05-09T15:57:33.713639+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3894**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3894, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/15 | 33.3% | +3.54% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.66% | **+0.49%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.79% | **+1.25%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.08% | **+0.87%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.63% | **+0.82%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.27% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 260件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T15:57:30.131950+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80486.9
- Funnel: target 769 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INX/USDT:USDT | +44.23% | $1,922,872.92 |
| PTB/USDT:USDT | +42.02% | $1,143,517.37 |
| SATO/USDT:USDT | +36.18% | $3,581,580.78 |
| SAHARA/USDT:USDT | +32.36% | $5,661,117.25 |
| ZEREBRO/USDT:USDT | +30.42% | $3,786,495.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.78% | +4.54% |
| H/USDT:USDT | below_1h_threshold | +4.25% | +4.00% |
| ORCA/USDT:USDT | below_1h_threshold | +4.24% | +4.00% |
| VVV/USDT:USDT | below_1h_threshold | +3.27% | +3.03% |
| BIO/USDT:USDT | below_1h_threshold | +2.93% | +2.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
