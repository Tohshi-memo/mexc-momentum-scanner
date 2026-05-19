# Decision Report

- generated_at: 2026-05-19T09:28:50.755813+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4466**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4466, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.04% | **+0.73%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.36% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +3.17% | **+1.81%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.01% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.29** / 初期 $100.00 (+24.29%)
- 確定: 463件 (Win 123 / Loss 158 / Flat 182) / skip 564件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $124.29

## 4. Latest Market Context

- 更新: 2026-05-19T09:28:48.742987+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=76736.2
- Funnel: target 763 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +33.68% | $9,635,599.53 |
| EDEN/USDT:USDT | +31.20% | $2,703,300.59 |
| PLAY/USDT:USDT | +24.82% | $3,263,910.11 |
| ONT/USDT:USDT | +13.35% | $1,122,314.34 |
| LIT/USDT:USDT | +10.96% | $1,300,182.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +3.74% | +4.10% |
| RON/USDT:USDT | below_1h_threshold | +2.13% | +2.49% |
| ONT/USDT:USDT | below_1h_threshold | +1.10% | +1.46% |
| SPACE/USDT:USDT | below_1h_threshold | +0.97% | +1.34% |
| CHZ/USDT:USDT | below_1h_threshold | +0.00% | +0.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
