# Decision Report

- generated_at: 2026-05-18T13:49:03.900309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4445**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4445, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.13% | **-0.06%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.39% | **+1.18%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.07% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.26** / 初期 $100.00 (+21.26%)
- 確定: 442件 (Win 115 / Loss 150 / Flat 177) / skip 564件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.38% 残高後 $121.26

## 4. Latest Market Context

- 更新: 2026-05-18T13:48:57.141574+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.85% price=76943.5
- Funnel: target 768 → liquid 130 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRAC/USDT:USDT | +49.51% | $1,158,246.99 |
| FIDA/USDT:USDT | +42.62% | $10,395,703.64 |
| BSB/USDT:USDT | +16.06% | $16,137,097.33 |
| OPENLEDGER/USDT:USDT | +12.87% | $1,590,289.07 |
| BILL/USDT:USDT | +7.09% | $33,341,260.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +3.80% | +4.65% |
| VVV/USDT:USDT | below_1h_threshold | +1.82% | +2.67% |
| PLAY/USDT:USDT | below_1h_threshold | +1.53% | +2.37% |
| GUA/USDT:USDT | below_1h_threshold | +0.74% | +1.59% |
| DISSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +1.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
