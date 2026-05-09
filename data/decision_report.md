# Decision Report

- generated_at: 2026-05-09T16:40:27.557439+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3902**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3902, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.30% | **-1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/15 | 53.3% | +0.71% | **+0.38%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.52% | **+0.18%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.04% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +4.82% | **+3.86%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.97% | **+2.23%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.26% | **+0.63%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 268件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T16:40:23.793347+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=80556.5
- Funnel: target 769 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +23.17% | $25,962,207.49 |
| SATO/USDT:USDT | +13.52% | $3,869,981.62 |
| OFC/USDT:USDT | +5.52% | $1,091,306.42 |
| BIO/USDT:USDT | +4.25% | $1,301,931.39 |
| ANTHROPIC/USDT:USDT | +3.84% | $1,309,401.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OFC/USDT:USDT | below_1h_threshold | +4.87% | +4.78% |
| BIO/USDT:USDT | below_1h_threshold | +4.26% | +4.17% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +3.84% | +3.76% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.33% | +3.24% |
| INX/USDT:USDT | below_1h_threshold | +3.31% | +3.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
